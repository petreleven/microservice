from requests import Session

s = Session()
key = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJkYXRhc2VydmljZS5ydW5uZXJ5LmNvbSJ9.kWE51gNJszI4ZGQKxozsmxo_qaBBQOUyaTInPV-kuvUGn5UmbcZw5vtUqyxtqxSNKTaY-AXsrbCJrkBRvg3bPGCOPuVu0dqvimsAdkhxkOFgHhFN30FQFfNLK_SLKZSztUh1Nl-vkLfeW-_qFeDDEClpCOsmjJiWAIgkkzQdEouOPkbdA0y--PXtrVOSDuSHBy4Od-aZvb1RzdZPUJSEXWHSf1ktxgsyOyGGU8kdAA0vecA4aFgQ6jbd1Dktwru0QcSE9wegYHIzZoWlb-pEiDdcT7vG1nH3GCGH6TTYtzvucfW2HDOn7myPe3M3Uf64EBWV70Zf_Z13jsblUNKqoYs4t42BMFAwP1vKFyQWwTwDWgPH3UkzBTiHq-BwEoK0ME73KMCcEN-Cegah-2oTYU4aDlz6h67MRpHX2ghWbxNfNYdhfEJKRlc36-hr8egExFs1CyFri51sMqFwHAOSvO6hCmfwmAIPowgSkfxYL2wRMHzJJWpeOlRBp8zVXTTiZzfGUZcEiIn2P7M_XKvprqxLPzLWKJkzI-N-SW5k9rIW7uM_buJtW9U4dGo3IRTlJBFxzvQD3FbPpTXQVh463oyPXyTjtfzMxT23DHvbvuZR1f0hDCWiPvf-tF8_aPhFx7pDoJsHlgibd986LvTZIBFufvLBz1kY9IwtbP3wERs"
s.headers = {"Authorization": f"Bearer {key}"}
resp = s.get("http://127.0.0.1:5002/getusers")
print(resp.json())
resp.close()