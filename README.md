
# OpenAI Conversations API Demo

This project demonstrates how to use the **OpenAI Conversations API** from Python to perform a complete conversation lifecycle: create, list items, retrieve, update, and delete a conversation.

## Overview
The `openai-api-conversations-ss.py` script is a simple but realistic flow using the official OpenAI Python SDK:

- Environment-based API key management for security.
- Create a conversation with metadata and an initial user message.
- List items in an existing conversation.
- Retrieve full conversation details by ID.
- Update conversation metadata (for example, change the topic).
- Delete a conversation and print the deletion response.
- Clean, well-documented code structure

The code prints clearly separated sections for each API call so the end‑to‑end behavior is easy to follow in the console. The demo focused on code structure easy to integrate into larger codebases.

## Prerequisites

Before running this project, ensure you have:

- Python 3.9 or higher
- An OpenAI API account and API key with access to the Conversations API ([sign up here](https://platform.openai.com/signup))
- pip (Python package manager)
- Internet connectivity to reach the OpenAI API endpoint

## Installation

1. **Clone the repository**

```bash
  git clone https://github.com/intarchs111/openai-api-conversations.git
  cd openai-api-conversations
```

2. **Install required dependencies**

Install dependencies
- 'openai' - Official OpenAI Python library
- 'python-dotenv' - Environment variable management

```bash
  pip install openai python-dotenv
```

3. **Set up your environment variables**

Create a '.env' file in the project root directory:
Add your OpenAI API key to the '.env' file:

**Important**: Never commit your '.env' file to version control. Add it to your '.gitignore' file.

   
## Configuration

You can modify the following parameters in `openai-api-conversations-ss.py`:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `topic` | The metadata to use | `"model conversations"` |
| `content` | The user message | `"Hello!"` |
| `limit` | The number of items returned when listing | `10` |


## Usage/Examples

Run the script from the command line:

```bash
  python openai-api-conversations-ss.py
```

You should see labeled sections similar to:
1. Create Conversation:
2. List Items:
3. Retrieve Conversation:
4. Update Conversation:
5. Delete Conversation:

![alt](/assets/openai-conv-api-demo.jpg)

## Security Best Practices

- Store API keys in environment variables, never hardcode them 
- Use `.env` files for local development 
- Add `.env` to your `.gitignore` file
- Consider using secret management tools for production environments

## Not in Scope

This project intentionally focuses on a minimal, self-contained demonstration of the OpenAI Responses API. The following are deliberately excluded to keep the example simple and focused:

*   **Production-grade error handling** (e.g., retries, rate limiting, API downtime recovery).
*   **Advanced authentication** (e.g., OAuth, service accounts, or multi-key rotation).
*   **Response storage/retrieval** when store=True (demo uses store=False).
*   **Logging, monitoring, or observability** integrations.
*   **Web UI, CLI interface, or input validation** for user prompts.
*   **Testing suite** (unit tests, integration tests).
*   **Containerization** (Docker) or deployment configurations (CI/CD, cloud providers).
*   **Multi-model support** or dynamic model selection.
*   **Cost tracking** or usage analytics.

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'openai'`
- **Solution**: Run `pip install openai python-dotenv`

**Issue**: `AuthenticationError: Invalid API key`
- **Solution**: Verify your API key in the `.env` file is correct and active

**Issue**: API response errors
- **Solution**: Check the [OpenAI API status page](https://status.openai.com/) and verify your account has available credits


## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - More examples and guides

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Suyog Hire: [LinkedIn](https://www.linkedin.com/suyoghire) \
**OpenAI Conversations API Demo** - Project Link: [GitHub](https://github.com/intarchs111/openai-api-conversations)

## Acknowledgments

This project utilizes established open-source libraries and official documentation to enable secure and efficient OpenAI API integration.
​
- **OpenAI Python SDK** – The official library for interacting with OpenAI APIs.
- **​OpenAI API Reference** – Comprehensive documentation for the Responses API endpoint.
- **​python-dotenv** – For loading environment variables from .env files securely.
