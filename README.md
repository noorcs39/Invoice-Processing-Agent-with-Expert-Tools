# 🤖 Invoice Processing Agent with Expert Tools

I am an AI-powered **Invoice Processing Agent**, designed to automate the classification and compliance validation of invoices using expert knowledge modules. My architecture is clean, modular, and easy to extend, making me ideal for modern finance workflows.

---

## 🧠 What I Do

I process raw invoice data and deliver structured, validated results through these key capabilities:

- ✅ **Extract Invoice Details**: I analyze and parse invoice text to identify vendor, items, amounts, and dates.  
- 🧾 **Categorize Expenditures**: I consult a financial categorization expert to assign each invoice to one of 20 predefined spending categories.  
- 🔍 **Validate Against Purchasing Rules**: I consult a compliance expert who checks invoices against the latest purchasing policy loaded from a human-readable file.  
- 📦 **Return Structured JSON Output**: I output a clean, structured summary with compliance status and issues, ready for databases or downstream systems.  
- 🗃️ **Store & Summarize**: I can log results and provide a quick summary of actions taken.

---

## 🛠️ Project Structure

```
invoice_processing_agent/
├── config/
│   └── purchasing_rules.txt       # Company rules for invoice validation
├── invoice_processing_agent.py    # Main agent and expert tool implementation
└── README.md                      # This file
```

---

## 🧪 Example

### 📄 Input Invoice:

```
Invoice #4567  
Date: 2025-02-01  
Vendor: Tech Solutions Inc.  
Items:  
  - Laptop - $1,200  
  - External Monitor - $300  
Total: $1,500  
```

### ✅ Output Summary:

```
Invoice #4567  
- Categorized as: IT Equipment  
- Compliance Check: Passed  
- Stored successfully  
```

---

## 📂 Installation & Usage

1. **Clone this repository**:

```bash
git clone https://github.com/yourusername/invoice-processing-agent.git
cd invoice-processing-agent
```

2. **Install any required dependencies** (ensure your LLM framework is set up).

3. **Add purchasing rules** in `config/purchasing_rules.txt`.

4. **Run the script**:

```bash
python invoice_processing_agent.py
```

---

## 🧩 Customization

- 🔄 **Add Categories**: Modify the `categories` list in `categorize_expenditure`.
- 📝 **Change Rules**: Edit `config/purchasing_rules.txt` — no code changes required.
- 🔗 **Integrate**: Use structured JSON output in workflows, databases, or reporting pipelines.

---

## 📜 License

MIT License. Free to use, adapt, and build upon.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or pull requests — especially for:

- New expert modules  
- Improved prompts  
- Workflow automation

---

## 🚀 Future Enhancements

- 🖨️ OCR support for scanned/PDF invoices  
- 🔐 Authentication & approval workflows  
- 📊 ERP & database integrations

---

> Built to be smart, adaptable, and easy to work with — like a real finance assistant.
