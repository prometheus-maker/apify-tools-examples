# Apify tools: PDF to Markdown, OCR, Website to Markdown crawler, SEO audit, Tech Stack

Working examples for my pay-per-use tools on the [Apify Store](https://apify.com/store).
Each one is an API: send URLs, get JSON back. You only pay for what you process, and there's no subscription.

| Tool | What it does | Price |
|---|---|---|
| 📄 [PDF & Document to Markdown](https://apify.com/prometheus-maker/pdf-document-to-markdown) | PDF, Word, PowerPoint, Excel, HTML, EPUB → clean Markdown for LLM / RAG. Tables, two-column papers, OCR for scans, chunking | $0.002 per document + $0.0002 per page |
| 🖼️ [Image & Scanned PDF to Text OCR](https://apify.com/prometheus-maker/image-to-text-ocr) | Text from photos, screenshots and scans in 41 languages, with line positions and confidence | $0.004 per image or page |
| 🕸️ [Website to Markdown Crawler](https://apify.com/prometheus-maker/website-to-markdown-crawler) | Crawl a site into clean Markdown for LLM / RAG: main content only, linked PDF/Word/Excel files converted too, optional chunks | $0.0015 per page |
| 🔎 [SEO Audit & Broken Link Checker](https://apify.com/prometheus-maker/website-seo-audit) | Audit every page of a site (titles, meta, headings, canonical, schema) and check every link and image for 404s. 0-100 score per page | $0.004 per page |
| 🌐 [Website Tech Stack Detector](https://apify.com/prometheus-maker/website-tech-stack-detector) | What a website is built with: CMS, frameworks, analytics, CDN, hosting, email provider. 7,000+ technologies (BuiltWith / Wappalyzer alternative) | $0.002 per website |
| 📸 [Website Screenshot API](https://apify.com/prometheus-maker/website-screenshot) | Full-page, first-screen, mobile or element screenshots as PNG, JPEG or PDF, cookie banners hidden | $0.005 per full page, $0.003 per first screen |
| 🔁 [HTTP Request Runner](https://apify.com/prometheus-maker/http-request-runner) | Send many API calls (GET/POST/any method) with retries and rate limits; status, headers and parsed JSON back | $0.001 per request |
| 📦 [Bulk File Downloader](https://apify.com/prometheus-maker/bulk-file-downloader) | Download files from URL lists or every file linked on a page; images, PDFs, media; optional ZIP | $0.0015 per file |
| 🎙️ [Audio & Video Transcriber](https://apify.com/prometheus-maker/audio-video-transcriber) | Speech to text with Whisper models: files, podcast feeds; text, timestamps, SRT | from $0.003 per audio minute |

Full prices, including per-page rates and discounts for paid Apify plans, are on each Store page.

## Quick start (curl)

Get an API token from [Apify Console → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/prometheus-maker~website-tech-stack-detector/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"urls": ["python.org"]}'
```

The same endpoint works for the other tools: replace the tool name and the input.

## Use them from Claude, Cursor or any MCP client

Every tool is also an MCP server, hosted by Apify (streamable HTTP). Add one to your client with your Apify token:

```json
{
  "mcpServers": {
    "pdf-to-markdown": {
      "url": "https://mcp.apify.com/?tools=prometheus-maker/pdf-document-to-markdown",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

Swap the part after `tools=` for any tool in the table (`prometheus-maker/website-to-markdown-crawler`, ...), or list
several separated by commas. The same entries are in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.prometheus-maker)
under `io.github.prometheus-maker/*` (files in [`mcp/`](mcp)). You pay per use, as with the API.

## Python

```bash
pip install apify-client
export APIFY_TOKEN=...
python python/pdf_to_markdown.py      # PDF → Markdown + RAG chunks
python python/image_to_text_ocr.py    # image → text
python python/tech_stack.py           # domains → technologies
python python/website_to_markdown.py  # website → Markdown pages + chunks
python python/seo_audit.py            # website → SEO scores, issues, broken links
```

The scripts are in [`python/`](python/). They use `apify-client` 3.x.

## Inputs at a glance

| Tool | Main input | Useful options |
|---|---|---|
| PDF to Markdown | `startUrls: [{"url": ...}]` | `chunkSize`, `outputFormat`, `pageRange`, `pdfPassword`, `ocrLanguages`, `includeTablesJson` |
| Image OCR | `imageUrls: [{"url": ...}]` | `languages` (e.g. `["eng","deu"]`), `engine`, `includeLines` (line positions) |
| Tech stack | `urls: ["example.com", ...]` | `checkDns` (email provider, verified tools), `includeEvidence` |
| Website to Markdown | `startUrls: ["https://example.com/docs/"]` | `maxPages`, `crawlScope`, `includeDocuments`, `chunkSize`, `keepLinks` |
| SEO audit | `startUrls: ["https://example.com"]` | `maxPages`, `checkExternalLinks`, `excludeUrlPatterns`, `maxLinkChecks` |

See each Store page for every field and a full output example.

## About

These tools are built and maintained by **Prometheus** ([notes](https://prometheus-maker.github.io/)). Issues and requests are welcome in this repo.
