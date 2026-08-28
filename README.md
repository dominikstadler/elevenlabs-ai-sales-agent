# 🎙️ ElevenLabs AI Sales Agent Simulator

An automated system designed to demonstrate how businesses can leverage Large Language Models (LLMs) and ElevenLabs' ultra-realistic Text-to-Speech (TTS) technology to create highly converting, personalized audio sales pitches at scale.

## 🚀 Features
- **Dynamic Script Generation:** Utilizes OpenAI's `gpt-4o-mini` to analyze products and target audiences to draft psychologically optimized cold-calling scripts.
- **Context-Aware Voice Synthesis:** Integrates ElevenLabs' `eleven_multilingual_v2` model to transform structural text into high-quality, emotionally engaging voice outputs.
- **Fail-safe Design:** Written with production-grade exception handling to ensure continuous execution even during API credential updates.

## 🛠️ Tech Stack
- **Core Language:** Python 3.10+
- **AI Voice Generation:** ElevenLabs API
- **LLM Context:** OpenAI API
- **Environment Management:** python-dotenv

## ⚙️ Quick Start Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd elevenlabs-ai-sales-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY="your-openai-api-key"
   ELEVENLABS_API_KEY="your-elevenlabs-api-key"
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
