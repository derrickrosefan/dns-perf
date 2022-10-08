const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');
const fs = require('fs');

const URLs = [
    "https://google.com",
    "https://youtube.com",
    "https://facebook.com",
    "https://amazon.com",
    "https://yahoo.com",
    "https://twitter.com",
    "https://instagram.com",
    "https://wikipedia.com",
    "https://reddit.com",
    "https://discord.com",
];

const NUM_RUNS_PER_URL = 10;
const FILE_PATH = "./results_public.json"

const test = async () => {
    const results = URLs.reduce((prev, url) => ({ ...prev, [url]: [] }), {});
    const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless'] });
    const options = { logLevel: 'info', output: 'html', onlyCategories: ['performance'], port: chrome.port };
    for (const url of URLs) {
        for (let i = 0; i < NUM_RUNS_PER_URL; i++) {
            console.log(`Run ${i + 1} out of ${NUM_RUNS_PER_URL} for ${url}`);
            const runnerResult = await lighthouse(url, options);
            const timeToInteractive = runnerResult.lhr.audits.interactive.numericValue / 1000;
            results[url].push(timeToInteractive);
        }
    }
    console.log(results);
    fs.writeFile(FILE_PATH, JSON.stringify(results), (err) => console.log(err));
    await chrome.kill();
}

test();