from blockfrost import BlockFrostApi, ApiError, ApiUrls
import os
from dotenv import load_dotenv

load_dotenv()

api = BlockFrostApi(
    project_id=os.getenv("BLOCKFROST_PROJECT_ID"),
    base_url=ApiUrls.mainnet.value,
)

try:
    address = "addr1qxvwaujuw3vky80h0j73xwh466q63zx6t67efvvz4npn6py52y9ckt97pxqvvp0d7an8hdtc2w3nvpxswfvd44q9cusqklxjqt"
    addr = api.address(address)

    for amount in addr.amount:
        if (amount.unit == "lovelace"):
            print(f'ADA balance on {address}: {int(amount.quantity) / 1000000} ADA')

except ApiError as e:
    print(e)
