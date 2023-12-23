import datetime


def main():
    last_run = datetime.datetime.fromisoformat("2023-12-23T13:08:14.786194Z")
    now = datetime.datetime.now(datetime.timezone.utc)
    print(now - last_run)


if __name__ == "__main__":
    main()
