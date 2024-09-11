# Financial Data Agent

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://financial-data-agent.streamlit.app/)

This repository contains a tool that processes financial reports, extracts key insights using LlamaIndex and OpenAI models, and provides a query interface for detailed financial data exploration.

**Note:** This tool specifically parses and analyzes the "Annual Report Government of Alberta 2023–2024."

## Features

- **Parse Financial Reports**: Automatically extracts financial information from company reports.
- **Query Engine**: Provides insights using GPT-4o powered models.
- **Numpy Storage**: Stores extracted nodes and objects for quick access.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Farhad-Davaripour/financial_data_agent.git
   cd financial_data_agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API keys to the `.env` file:
   ```bash
   LLAMA_CLOUD_API_KEY=your_llama_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the script to parse financial reports and query data:
```bash
python main.py
```

## License

This project is licensed under the MIT License.
