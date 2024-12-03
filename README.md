# Process Flow Mapper

A comprehensive Streamlit application for creating and visualizing process flows using both Graphviz and Mermaid.js. The application supports natural language processing to convert text descriptions into process diagrams.

## Features

- Create process flow diagrams using Graphviz
- Generate Mermaid.js state diagrams
- Natural language processing support
- Multiple theme options
- Export diagrams in various formats (PNG, SVG, JPG)
- Support for complex decision trees and branching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gilbert-mjp/process-flow-mapper.git
cd process-flow-mapper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Install Graphviz:
- Windows: Download from [Graphviz Official Site](https://graphviz.org/download/)
- Linux: `sudo apt-get install graphviz`
- macOS: `brew install graphviz`

4. Set up your Anthropic API key:
```bash
export ANTHROPIC_API_KEY=your-api-key
```

## Usage

1. Run the Graphviz-based process mapper:
```bash
streamlit run src/process_mapper_app.py
```

2. Run the Mermaid-based process mapper:
```bash
streamlit run src/process_mapper_mermaid.py
```

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.