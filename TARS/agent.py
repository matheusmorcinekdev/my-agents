from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from TARS.tools import get_special_message, call_node_script, get_bitcoin_price, fetch_calendar_events

from TARS.prompt import DB_MCP_PROMPT

root_agent = Agent(
    name="TARS",
    model="gemini-2.0-flash",
    description="TARS from Interstellar movie",
    instruction=DB_MCP_PROMPT,
    tools=[get_special_message, 
           call_node_script, 
           get_bitcoin_price,
           fetch_calendar_events,
           MCPToolset(
                connection_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@modelcontextprotocol/server-puppeteer"]
                )
           )]
)