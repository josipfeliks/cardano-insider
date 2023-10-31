from blockfrost import BlockFrostApi, ApiError, ApiUrls
import os
from dotenv import load_dotenv

load_dotenv()

api = BlockFrostApi(
    project_id=os.getenv("BLOCKFROST_PROJECT_ID"),
    base_url=ApiUrls.mainnet.value,
)

print(os.environ["BLOCKFROST_PROJECT_ID"])
