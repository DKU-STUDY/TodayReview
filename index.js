const axios = require("axios");
const dayjs = require("dayjs");

axios.post(`https://api.github.com/repos/${process.env.REPO}/issues`, {
  title: dayjs().format("YYYY MM DD"),
  body: ''
}, {
  headers: {
    authorization: `Bearer ${process.env.TOKEN}`
  }
}).then(({ data }) => console.log(data));
