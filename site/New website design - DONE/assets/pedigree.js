/* Pedigree Catalog — builds the spine, detail panel, and Leaflet maps */
(function(){
  const data = window.ANCESTORS || [];
  const ancestors = data.filter(d => d.type === 'ancestor');
  const eras = data.filter(d => d.type === 'era');

  const ERA_LABEL = {
    'era-norman':'Norman','era-medieval':'Medieval','era-tudor':'Tudor',
    'era-emigrant':'Emigrant','era-gilded':'Gilded','era-modern':'Modern'
  };
  const eraColor = (era) => {
    const s = getComputedStyle(document.documentElement);
    return {
      a: s.getPropertyValue('--' + era + '-a').trim() || '#8a4b1e',
      b: s.getPropertyValue('--' + era + '-b').trim() || '#ae6539',
      tint: s.getPropertyValue('--' + era + '-tint').trim() || '#f5e6d4'
    };
  };

  // ---------------- stats ----------------
  const allPlaces = new Set();
  const allHoldings = new Set();
  ancestors.forEach(a => {
    (a.locations || []).forEach(l => allPlaces.add(l.place));
    (a.landHoldings || []).forEach(h => allHoldings.add(h.split(' (')[0]));
  });
  document.getElementById('stat-places').textContent = allPlaces.size;
  document.getElementById('stat-holdings').textContent = allHoldings.size;

  // ---------------- spine ----------------
  const spine = document.getElementById('spine');
  // Walk data array in its given order, grouping ancestors under preceding era divider
  function buildSpine(filterEra, filterStatus){
    spine.innerHTML = '';
    let currentEra = null;
    let currentBand = null;
    let visibleCount = 0;
    data.forEach((item) => {
      if (item.type === 'era') {
        currentEra = item;
        currentBand = null; // lazy-create when first ancestor matches
        return;
      }
      if (item.type !== 'ancestor') return;
      if (filterEra !== 'all' && item.era !== filterEra) return;
      if (filterStatus !== 'all' && item.lineageStatus !== filterStatus) return;

      if (!currentBand && currentEra) {
        const col = eraColor(currentEra.cssClass);
        const band = document.createElement('div');
        band.className = 'era-band';
        band.style.background = `linear-gradient(90deg, ${col.a}, ${col.b})`;
        band.innerHTML = `<span>${currentEra.label}</span><span class="era-range">${currentEra.from} – ${currentEra.to}</span>`;
        spine.appendChild(band);
        currentBand = band;
      }

      const col = eraColor(item.era);
      const row = document.createElement('div');
      row.className = 'pedigree-row';
      row.dataset.gen = item.gen;
      row.style.setProperty('--a', col.a);
      row.style.setProperty('--b', col.b);
      row.style.setProperty('--tint', col.tint);
      row.innerHTML = `
        <div class="gen-badge">${item.gen}</div>
        <div class="timeline-dot"><span class="dot"></span></div>
        <div class="name-block">
          <div class="name-text" style="font-family:var(--serif);font-size:1.08rem;font-weight:500;color:var(--ink);letter-spacing:-.005em">${item.name}</div>
          <div class="summary-line" style="font-family:var(--sans);font-size:12.5px;color:var(--muted);margin-top:3px;line-height:1.4">${item.dates} · ${item.geography}</div>
        </div>
        <div class="row-meta" style="display:flex;flex-direction:column;gap:4px;align-items:flex-end">
          <span class="status-tag ${item.lineageStatus === 'Confirmed' ? 'confirmed' : ''}" style="font-family:var(--sans);font-size:10px;letter-spacing:.06em;text-transform:uppercase;padding:2px 7px;border:1px solid var(--rule-2);border-radius:999px;color:var(--muted);font-weight:700">${item.lineageStatus}</span>
          <span class="chevron">›</span>
        </div>
      `;
      row.addEventListener('click', () => selectAncestor(item.gen));
      spine.appendChild(row);
      visibleCount++;
    });
    document.getElementById('result-count').textContent = `${visibleCount} ancestor${visibleCount === 1 ? '' : 's'}`;
  }

  // ---------------- detail panel ----------------
  let miniMap = null;
  let currentSelection = null;

  function selectAncestor(gen) {
    const a = ancestors.find(x => x.gen === gen);
    if (!a) return;
    currentSelection = gen;
    try { localStorage.setItem('gurney-active-gen', gen); } catch {}

    document.querySelectorAll('.pedigree-row').forEach(r => r.classList.toggle('active', r.dataset.gen === gen));

    const panel = document.getElementById('detail-panel');
    const col = eraColor(a.era);
    panel.innerHTML = `
      <div class="detail-head" style="padding:18px 22px 14px;border-bottom:1px solid var(--rule-2);background:linear-gradient(180deg, ${col.tint} 0%, transparent 100%)">
        <span class="era-tag" style="display:inline-block;font-family:var(--sans);font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;padding:3px 9px;border-radius:4px;background:linear-gradient(90deg, ${col.a}, ${col.b})">${ERA_LABEL[a.era] || a.era} · ${a.gen}</span>
        <h2 style="font-family:var(--serif);font-size:1.55rem;font-weight:600;margin:8px 0 4px;letter-spacing:-.015em;color:var(--ink)">${a.name}</h2>
        <p style="font-family:var(--sans);font-size:12.5px;color:var(--muted);margin:0">${a.dates} · ${a.geography}</p>
      </div>
      <div class="detail-body" style="padding:16px 22px 20px;display:flex;flex-direction:column;gap:14px">
        <p style="font-family:var(--serif);font-size:1.02rem;line-height:1.5;color:var(--ink-soft);margin:0;text-wrap:pretty">${a.summary}</p>

        <div class="mini-map-wrap"><div class="mini-map" id="mini-map"></div></div>

        <div>
          <h4 style="font-family:var(--sans);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:0 0 6px">Highlights</h4>
          <ul style="font-family:var(--serif);font-size:14.5px;margin:0;padding-left:18px;line-height:1.5;color:var(--ink-soft)">
            ${(a.highlights || []).map(h => `<li>${h}</li>`).join('')}
          </ul>
        </div>

        <div>
          <h4 style="font-family:var(--sans);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:0 0 6px">Land &amp; holdings</h4>
          <ul style="font-family:var(--serif);font-size:14px;margin:0;padding-left:18px;line-height:1.5;color:var(--ink-soft)">
            ${(a.landHoldings || []).map(h => `<li>${h}</li>`).join('')}
          </ul>
        </div>

        ${(a.spouses && a.spouses.length) ? `
        <div>
          <h4 style="font-family:var(--sans);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:0 0 6px">Spouse</h4>
          <div style="font-family:var(--serif);font-size:14px;color:var(--ink-soft)">${a.spouses.map(s => `${s.name}${s.dates ? ' — ' + s.dates : ''}`).join('; ')}</div>
        </div>` : ''}

        ${(a.children && a.children.length) ? `
        <div>
          <h4 style="font-family:var(--sans);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:0 0 6px">Issue (direct heir)</h4>
          <div style="font-family:var(--serif);font-size:14px;color:var(--ink-soft)">${a.children.map(c => `${c.name}${c.notes ? ' — ' + c.notes : ''}`).join('; ')}</div>
        </div>` : ''}

        <div class="detail-actions" style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">
          <a class="btn primary" href="${a.factSheet || 'fact-sheet.html'}" style="font-family:var(--sans);font-size:12.5px;padding:7px 14px;border-radius:7px;background:var(--accent);color:#fff;border:1px solid var(--accent);font-weight:600;text-decoration:none">Open fact sheet →</a>
          <button class="btn" type="button" data-action="focus-map" style="font-family:var(--sans);font-size:12.5px;padding:7px 14px;border-radius:7px;background:var(--paper);color:var(--ink);border:1px solid var(--rule);font-weight:600">View on full map</button>
        </div>
      </div>
    `;

    // mini-map
    setTimeout(() => renderMiniMap(a), 50);

    panel.querySelector('[data-action="focus-map"]')?.addEventListener('click', () => {
      switchView('map');
      setTimeout(() => focusOnAncestor(a), 200);
    });
  }

  function renderMiniMap(a) {
    const el = document.getElementById('mini-map');
    if (!el) return;
    if (miniMap) { miniMap.remove(); miniMap = null; }
    const locs = (a.locations || []).filter(l => l.lat && l.lng);
    if (!locs.length) { el.parentElement.innerHTML = '<div style="font-family:var(--sans);font-size:12px;color:var(--muted);padding:20px;text-align:center">No coordinates for this ancestor.</div>'; return; }
    miniMap = L.map(el, { zoomControl: false, attributionControl: false, scrollWheelZoom: false }).setView([locs[0].lat, locs[0].lng], 7);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { maxZoom: 18 }).addTo(miniMap);
    const col = eraColor(a.era);
    const bounds = [];
    locs.forEach(l => {
      const holdings = (a.landHoldings || []).map(h => h.toLowerCase());
      const isHolding = holdings.some(h => h.includes(l.place.toLowerCase()));
      const marker = makeMarker(l, col, isHolding);
      marker.addTo(miniMap);
      marker.bindPopup(`<div class="pop-title">${l.place}</div><div class="pop-meta">${isHolding ? 'Holding' : 'Residence / role'}${l.label ? ' · ' + l.label : ''}</div>`);
      bounds.push([l.lat, l.lng]);
    });
    if (bounds.length > 1) miniMap.fitBounds(bounds, { padding: [24, 24] });
  }

  // Custom divIcon markers: circles = role/residence, squares = holdings, era-colored
  function makeMarker(loc, col, isHolding) {
    const fill = col.a;
    const html = isHolding
      ? `<span style="display:block;width:14px;height:14px;background:${fill};border:2px solid #fff;box-shadow:0 0 0 1px rgba(0,0,0,.25)"></span>`
      : `<span style="display:block;width:14px;height:14px;border-radius:50%;background:${fill};border:2px solid #fff;box-shadow:0 0 0 1px rgba(0,0,0,.25)"></span>`;
    const icon = L.divIcon({ html, className: 'gurney-marker', iconSize: [14,14], iconAnchor: [7,7] });
    return L.marker([loc.lat, loc.lng], { icon });
  }

  // ---------------- full map ----------------
  let fullMap = null;
  function buildFullMap() {
    if (fullMap) return;
    fullMap = L.map('full-map', { scrollWheelZoom: true }).setView([51.2, 0.9], 5);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { maxZoom: 18, attribution: '© OpenStreetMap · © CARTO' }).addTo(fullMap);

    // Aggregate places → show a marker per (place, ancestor, role)
    const all = [];
    ancestors.forEach(a => {
      const col = eraColor(a.era);
      const holdings = (a.landHoldings || []).map(h => h.toLowerCase());
      (a.locations || []).forEach(l => {
        if (!l.lat || !l.lng) return;
        const isHolding = holdings.some(h => h.includes(l.place.toLowerCase()));
        all.push({ loc: l, ancestor: a, col, isHolding });
      });
    });

    // Draw the father-to-son path using principal seats (first location of each ancestor)
    const seatPath = ancestors.slice().reverse()
      .map(a => (a.locations || [])[0])
      .filter(l => l && l.lat && l.lng)
      .map(l => [l.lat, l.lng]);
    if (seatPath.length > 1) {
      L.polyline(seatPath, { color: '#8a4b1e', weight: 2, opacity: .55, dashArray: '4 4' }).addTo(fullMap);
    }

    all.forEach(row => {
      const m = makeMarker(row.loc, row.col, row.isHolding);
      m.bindPopup(`
        <div class="pop-title">${row.loc.place}${row.loc.label ? ' <span style="color:var(--muted);font-weight:400">· ' + row.loc.label + '</span>' : ''}</div>
        <div class="pop-meta">${row.isHolding ? 'Land holding' : 'Residence / role'}</div>
        <div class="pop-people"><span><span class="pg">${row.ancestor.gen}</span>${row.ancestor.name}</span></div>
      `);
      m.addTo(fullMap);
      row._marker = m;
    });

    // fit to all
    const group = L.featureGroup(all.map(r => r._marker));
    fullMap.fitBounds(group.getBounds(), { padding: [32, 32] });

    // Side people list
    const side = document.getElementById('map-people');
    side.innerHTML = '';
    ancestors.forEach(a => {
      const col = eraColor(a.era);
      const row = document.createElement('div');
      row.className = 'map-person-row';
      row.style.setProperty('--a', col.a);
      row.style.setProperty('--b', col.b);
      row.innerHTML = `
        <div class="bar"></div>
        <div class="gen-s">${a.gen}</div>
        <div class="n">${a.name}</div>
        <div class="d">${a.dates.replace(/^c\. /, '').replace(/^fl\. /, '')}</div>
      `;
      row.addEventListener('click', () => focusOnAncestor(a));
      side.appendChild(row);
    });
  }

  function focusOnAncestor(a) {
    buildFullMap();
    const locs = (a.locations || []).filter(l => l.lat && l.lng);
    if (!locs.length) return;
    if (locs.length === 1) fullMap.setView([locs[0].lat, locs[0].lng], 8);
    else fullMap.fitBounds(locs.map(l => [l.lat, l.lng]), { padding: [60, 60] });
  }

  // ---------------- view switch ----------------
  function switchView(v) {
    document.querySelectorAll('.view-switch button').forEach(b => b.classList.toggle('active', b.dataset.view === v));
    document.getElementById('catalog-view').style.display = v === 'list' ? '' : 'none';
    const mv = document.getElementById('map-view');
    mv.classList.toggle('active', v === 'map');
    if (v === 'map') {
      setTimeout(() => { buildFullMap(); if (fullMap) fullMap.invalidateSize(); }, 50);
    }
  }
  document.querySelectorAll('.view-switch button').forEach(b => {
    b.addEventListener('click', () => switchView(b.dataset.view));
  });

  // ---------------- filters ----------------
  let filterEra = 'all', filterStatus = 'all';
  document.querySelectorAll('#era-filter button').forEach(b => {
    b.addEventListener('click', () => {
      document.querySelectorAll('#era-filter button').forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      filterEra = b.dataset.era;
      buildSpine(filterEra, filterStatus);
      if (currentSelection) selectAncestor(currentSelection);
    });
  });
  document.querySelectorAll('#status-filter button').forEach(b => {
    b.addEventListener('click', () => {
      document.querySelectorAll('#status-filter button').forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      filterStatus = b.dataset.status;
      buildSpine(filterEra, filterStatus);
      if (currentSelection) selectAncestor(currentSelection);
    });
  });

  // ---------------- ruler ----------------
  function buildRuler() {
    const host = document.getElementById('ruler-inner');
    if (!host) return;
    const fromY = 1000, toY = 2000;
    for (let y = 1100; y <= 1900; y += 100) {
      const pct = 100 - ((y - fromY) / (toY - fromY)) * 100;
      const t = document.createElement('div');
      t.className = 'ruler-tick';
      t.style.top = pct + '%';
      t.innerHTML = `<div class="year">${y}</div><div class="era-mark" style="background:${eraMarkFor(y)}"></div>`;
      host.appendChild(t);
    }
  }
  function eraMarkFor(y) {
    const hit = eras.find(e => y >= e.from && y <= e.to);
    if (!hit) return 'transparent';
    const c = eraColor(hit.cssClass);
    return `linear-gradient(90deg, ${c.a}, ${c.b})`;
  }

  // ---------------- boot ----------------
  buildSpine('all', 'all');
  buildRuler();

  // Restore last selection
  let initial = null;
  try { initial = localStorage.getItem('gurney-active-gen'); } catch {}
  if (initial && ancestors.find(a => a.gen === initial)) selectAncestor(initial);
  else selectAncestor('G20');

  // Deep link ?gen=G20
  const params = new URLSearchParams(location.search);
  if (params.get('gen')) {
    const g = params.get('gen');
    if (ancestors.find(a => a.gen === g)) selectAncestor(g);
  }
})();
