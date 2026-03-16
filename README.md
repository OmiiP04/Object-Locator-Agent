# Object Locator Assistant

A voice-controlled AI assistant that helps you locate objects in an inventory system using natural language queries and speech recognition.

## Features

- **Voice Input**: Speak your queries naturally (e.g., "Where is the laptop?")
- **Voice Output**: Get spoken responses for hands-free operation
- **Interactive GUI**: Clean, user-friendly interface with chat history
- **AI-Powered**: Uses Google's Gemini AI for intelligent responses
- **Dummy Inventory**: Pre-loaded with sample inventory data for demonstration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/object-locator-agent.git
   cd object-locator-agent
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Google AI API key: `Apikey=your_api_key_here`

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application
2. Click the "🎤 Ask" button
3. Speak your query (e.g., "Where is the monitor?")
4. The assistant will respond with the location and speak it aloud

## Supported Objects

The assistant can locate items in these categories:
- Electronics (laptops, monitors, keyboards, etc.)
- Office Supplies (notebooks, pens, staplers, etc.)
- Networking & Power (cables, adapters, UPS, etc.)
- Miscellaneous (office chairs, etc.)

## Requirements

- Python 3.13+
- Microphone for voice input
- Speakers/headphones for voice output
- Google AI API key

## Troubleshooting

- Ensure your microphone is properly configured
- Check that your API key is valid and has sufficient quota
- Make sure all dependencies are installed correctly

## License

MIT License