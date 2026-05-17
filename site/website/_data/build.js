module.exports = () => {
  const now = new Date();
  const formatter = new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "long", year: "numeric" });
  return { date: formatter.format(now) };
};
