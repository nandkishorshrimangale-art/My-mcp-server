from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("SimpleMCPServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    """
    return a * b

@mcp.tool()
def greet(name: str) -> str:
    """
    Greet a user.
    """
    return f"Hello, {name}! Welcome to the MCP Server."

@mcp.tool()
def square(number: int) -> int:
    """
    Return the square of a number.
    """
    return number * number

if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run()
