from .round_manager import RoundManager

class Engine:
    def __init__(self, config, modules, logger=print):
        self.config = config
        self.modules = modules
        self.logger = logger
        self.round_manager = RoundManager(config["global_rounds"])

    def run(self):
        accounts = [a for a in self.config["accounts"] if a.get("enabled", True)]
        order = self.config.get("feature_order", [])

        for round_no in range(1, self.round_manager.rounds + 1):
            self.logger(f"ROUND {round_no}/{self.round_manager.rounds}")

            for account in accounts:
                self.logger(f"APP {account['id']} START")

                for feature_name in order:
                    settings = account.get("features", {}).get(feature_name, {})
                    if not settings.get("enabled", False):
                        continue

                    module = self.modules.get(feature_name)
                    if module is None:
                        self.logger(f"SKIP {feature_name}: module not installed")
                        continue

                    limit = int(settings.get("limit", 0))
                    if limit <= 0:
                        continue

                    self.logger(
                        f"RUN {feature_name} account={account['id']} limit={limit}"
                    )
                    module.run(account=account, limit=limit)

                self.logger(f"APP {account['id']} DONE")

        self.logger("ALL ROUNDS DONE")
