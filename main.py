# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import asyncio
from shared_client import start_client
import importlib
import os
import sys

async def load_and_run_plugins():
    # Start the client
    await start_client()
    
    # Define plugin directory
    plugin_dir = "plugins"
    
    # Get the list of plugin files, excluding __init__.py
    plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]
    
    # Iterate over plugins and run their associated functions
    for plugin in plugins:
        module = importlib.import_module(f"plugins.{plugin}")
        
        # Check if the plugin has the function to run
        if hasattr(module, f"run_{plugin}_plugin"):
            print(f"Running {plugin} plugin...")
            await getattr(module, f"run_{plugin}_plugin")()  
        else:
            print(f"{plugin} does not have the required function run_{plugin}_plugin")

async def main():
    await load_and_run_plugins()
    while True:
        await asyncio.sleep(1)  # Keep the script running

if __name__ == "__main__":
    print("Starting clients ...")
    try:
        # Use asyncio.run to handle the event loop
        asyncio.run(main())  # This will automatically manage the event loop
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
