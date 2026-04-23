from mcp.server.fastmcp import FastMCP
import os

# 1. 创建MCP服务
mcp = FastMCP("MyCustomMCP")

# 2. 注册工具（加@mcp.tool()即可）
@mcp.tool()
def get_desktop_files() -> list:
    """获取桌面文件列表"""
    return os.listdir(os.path.expanduser("~/Desktop"))

@mcp.tool()
def calculator(a: float, b: float, operator: str) -> float:
    """基础计算器，支持 + - * /"""
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/": return a / b
    raise ValueError("仅支持 + - * /")

# 3. 启动服务（stdio模式）
if __name__ == "__main__":
    mcp.run(transport="stdio")