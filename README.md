# Lewis Hamilton F1 Stats — Web Scraper & Power BI Dashboard

A Python web scraper that collects Lewis Hamilton's full Formula 1 race history from [motorsportstats.com](https://www.motorsportstats.com) and exports it to Excel for analysis in a Power BI dashboard.

---

## What It Does

1. Scrapes all pages of Hamilton's F1 race starts from motorsportstats.com
2. Parses the HTML stats table from each page using BeautifulSoup
3. Combines all pages into a single dataset
4. Exports the data to Excel for use in Power BI

---

## Tech Stack

| Purpose | Library |
|---|---|
| HTTP requests | requests |
| HTML parsing | BeautifulSoup4 |
| Data processing | pandas |
| Export | pandas |
| Visualisation | Power BI Desktop |

---

## Dashboard Preview

<img width="1073" height="602" alt="obraz" src="https://github.com/user-attachments/assets/b3e4aeb4-27d4-44cf-984d-7b4a7c768622" />


The dashboard includes:
- Race results across Hamilton's full F1 career
- Win count by season
- Podiums, poles and other key stats by year

---

## How It Works

motorsportstats.com paginates Hamilton's race history across 4 pages. The script iterates over all page URLs, scrapes the stats table from each, and concatenates the results into one DataFrame.

```
Page 1 ──┐
Page 2 ──┤──> scrape table ──> combine ──> export to Excel ──> Power BI
Page 3 ──┤
Page 4 ──┘
```

---

## Known Limitations

- The page URLs are hardcoded — if motorsportstats.com changes its pagination structure the URLs will need updating
- No error handling for failed requests — if one page returns a non-200 response the script will crash on `table.find_all()`
- The site may block automated requests over time;

---

## License

MIT
