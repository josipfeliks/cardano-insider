from blockfrost import BlockFrostApi, ApiError, ApiUrls
import os
from dotenv import load_dotenv
import codecs

def dissect_address(api, address):
    try:
        addr = api.address(address)
        decode_hex = codecs.getdecoder("hex_codec")

        for amount in addr.amount:
            if (amount.unit == "lovelace"):
                print(f'ADA balance on {address}: {int(amount.quantity) / 1000000} ADA')
            else:

                policy_id = amount.unit[0:56]
                data = api.assets_policy(policy_id)
                asset_name = decode_hex(amount.unit[56:])[0]

                if (len(data) != 1):
                    print(f"NFT {asset_name}")
                else:
                    print(f"Native token {asset_name}: {amount.quantity}")

    except ApiError as e:
        print(e)

def main():
    load_dotenv()

    api = BlockFrostApi(
        project_id=os.getenv("BLOCKFROST_PROJECT_ID"),
        base_url=ApiUrls.mainnet.value,
    )

    address = "addr1qxvwaujuw3vky80h0j73xwh466q63zx6t67efvvz4npn6py52y9ckt97pxqvvp0d7an8hdtc2w3nvpxswfvd44q9cusqklxjqt"
    dissect_address(api, address)

if __name__ == "__main__":
    main()
