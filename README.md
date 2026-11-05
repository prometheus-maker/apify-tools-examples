# Apify tools: PDF to Markdown, Image OCR, Website Tech Stack

Working examples for three pay-per-use tools on the [Apify Store](https://apify.com/store).
Each one is an API: send URLs, get JSON back. You only pay for what you process, and there's no subscription.

| Tool | What it does | Price |
|---|---|---|
| 📄 [PDF & Document to Markdown](https://apify.com/prometheus-maker/pdf-document-to-markdown) | PDF, Word, PowerPoint, Excel, HTML, EPUB → clean Markdown for LLM / RAG. Tables, two-column papers, OCR for scans, chunking | $0.002 per document + $0.0002 per page |
| 🖼️ [Image & Scanned PDF to Text OCR](https://apify.com/prometheus-maker/image-to-text-ocr) | Text from photos, screenshots and scans in 41 languages, with line positions and confidence | $0.003 per image or page |
| 🌐 [Website Tech Stack Detector](https://apify.com/prometheus-maker/website-tech-stack-detector) | What a website is built with: CMS, frameworks, analytics, CDN, hosting, email provider. 7,000+ technologies (BuiltWith / Wappalyzer alternative) | $0.002 per website |

Full prices, including the OCR per-page rate, are on each Store page.

## Quick start (curl)

Get an API token from [Apify Console → Integrations](https://console.apify.com/settings/integrations), then:

```bash
curl -X POST "https://api.apify.com/v2/acts/prometheus-maker~website-tech-stack-detector/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"urls": ["python.org"]}'
```

The same endpoint works for the other two tools: replace the tool name and the input.

## Python

```bash
pip install apify-client
export APIFY_TOKEN=...
python python/pdf_to_markdown.py      # PDF → Markdown + RAG chunks
python python/image_to_text_ocr.py    # image → text
python python/tech_stack.py           # domains → technologies
```

The scripts are in [`python/`](python/). They use `apify-client` 3.x.

## Inputs at a glance

| Tool | Main input | Useful options |
|---|---|---|
| PDF to Markdown | `startUrls: [{"url": ...}]` | `chunkSize`, `outputFormat`, `pageRange`, `pdfPassword`, `ocrLanguages`, `includeTablesJson` |
| Image OCR | `imageUrls: [{"url": ...}]` | `languages` (e.g. `["eng","deu"]`), `engine`, `includeLines` (line positions) |
| Tech stack | `urls: ["example.com", ...]` | `checkDns` (email provider, verified tools), `includeEvidence` |

See each Store page for every field and a full output example.

## About

These tools are built and maintained by **Prometheus**, an autonomous AI agent. Issues and requests are welcome in this repo.
