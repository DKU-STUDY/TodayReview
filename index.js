const axios = require("axios");
const dayjs = require("dayjs");

const githubClient = axios.create({
  baseURL: `https://api.github.com/repos/${process.env.REPO}`,
  timeout: 5000,
  headers: { authorization: `Bearer ${process.env.TOKEN}` }
});

githubClient.interceptors.response.use(({ data }) => data, error => Promise.reject(error));

function fetchIssues() {
  return githubClient.get(`/issues`);
}

function postIssue() {
  return githubClient.post(`/issues`, {
    title: dayjs().format("YYYY MM DD"),
    body: ''
  });
}

async function main() {
  const issues = (await fetchIssues()) || [];
  await Promise.all(issues.map(({ number }) =>
    githubClient.patch(`/issues/${number}`, { state: 'closed' })
  ));
  return postIssue()
}

main().then(console.log);
