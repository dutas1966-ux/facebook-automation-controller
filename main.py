import json
from pathlib import Path

from core.engine import Engine
from core.logger import log

CONFIG = Path(__file__).parent / "config" / "config.json"

def load_config():
    return json.loads(CONFIG.read_text(encoding="utf-8"))

if __name__ == "__main__":
    config = load_config()
    # Modules are intentionally empty adapters in this starter skeleton.
    Engine(config, modules={}, logger=log).run()
