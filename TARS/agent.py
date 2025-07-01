from pathlib import Path
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from TARS.tools import get_special_message, call_node_script, get_bitcoin_price

from TARS.prompt import DB_MCP_PROMPT

LOCAL_MPC_TEST_PATH = str((Path(__file__).parent.parent / "local_mcp" / "index.js").resolve())

root_agent = Agent(
    name="TARS",
    model="gemini-2.0-flash",
    description="TARS from Interstellar movie",
    instruction=DB_MCP_PROMPT,
    tools=[get_special_message, 
           call_node_script, 
           get_bitcoin_price,
           MCPToolset(
                connection_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@modelcontextprotocol/server-puppeteer"],
                    env={
                        "PUPPETEER_LAUNCH_OPTIONS": '{"headless": true, "timeout": 30000, "defaultViewport": {"width": 375, "height": 812, "deviceScaleFactor": 3, "isMobile": true, "hasTouch": true, "isLandscape": false}, "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}',
                        "ALLOW_DANGEROUS": "true"
                    }
                )
           ),
           MCPToolset(
               connection_params=StdioServerParameters(
                   command="node",
                   args=[LOCAL_MPC_TEST_PATH]
               )
           )]
)