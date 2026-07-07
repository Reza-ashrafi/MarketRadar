from config.settings import PROJECT_NAME
from collectors.symbol_collector import SymbolCollector


def main():

    print(f"{PROJECT_NAME} Started")

    try:
        collector = SymbolCollector()

        data = collector.collect()

        print("TSETMC Connected")

        print(type(data))

        print(data.keys())

    except Exception as e:
        print("ERROR:")
        print(e)


if __name__ == "__main__":
    main()
