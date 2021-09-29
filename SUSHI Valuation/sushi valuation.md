# General Valuation
Based on what I researched, these are some metrics that analysts use to evaluate a token's performance and I added some of my own.

| Metrics              | Formula     | What it means for SUSHI?             |
| -------------------- | ---------------- | ----------------------- |
| Price-to-Sales       | Fully Dil. Market Capitalization/Annualized Total Revenue    | Gives a bearing on the current market valuation of SUSHI wrt SushiSwap total revenue |
| Price-to-Earnings    | Fully Dil. Market Capitalization/Annualized Protocol Revenue | Gives a bearing on the current market valuation of SUSHI wrt revenues earned by staking SUSHI for xSUSHI |
| Price-to-RevStream   | Fully Dil. Market Capitalization/Annualized Specific Revenue | Gives a bearing on the current market valuation of SUSHI wrt Specific Revenue Stream (Lending, yield, LP etc.) |
| Price-to-Volume      | Fully Dil. Market Capitalization/Swap Volume | Gives a bearing on the current market valuation of SUSHI wrt Swapping Activity |
| Total Value Locked (TVL) | Total market valuation of tokens locked within a Protocol Ecosystem | Tells us how many assets are sitting in SushiSwap's contracts |
| Adjusted TVL        | Same as TVL but setting a locked price to discount market price volatility | Tells us the true movement of assets in/out of SushiSwap's contracts | 
| (Adj/Non-Adj) Un-incentivised TVL | Same as TVL but only without counting yield farming | Allows us to compare between protocols that do not offer yield farming |
| (Adj/Non-Adj) Incentivised TVL | Same as TVL but only counting yield farming | Allows us to compare between protocols that do offer yield farming |
| Revenue-to-Locked  | Total Revenue/TVL | Tells us how good SushiSwap is able to generate revenue on capital (swapping activity, yields etc.) |
| Total Market Share | Protocol's Total Revenue as a percentage of Total Market Revenue of similar Protocols | Gives a bearing on the size of SushiSwap within the same sector |
| Chain Market Share | Same as total market share but specified by Chain | Gives a bearing on the size of SushiSwap within the same sector but by chain dominance |
| Unique Wallet Activity (& holding) | Calculate the number of unique wallets that interact with the Protocol | Gives an indication of SushiSwap's user growth |


# Specific Activity Valuation
I think it is useful to also understand what sort of activities are taking place within a Protocol. Understanding them can provide us with additional tools to aid us in valuing Protocol's Token.

| Activity              | Related dApp     | Input Token             | Output Token                                  | Revenue                                                                                        |
| --------------------  | ---------------- | ----------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Pair Isolated Lending | Kashi            | Supplying Token         | Specific Kashi Medium-risk Pair (KMP) Token   | Interests in Supplied Token, 10% of Interests and Closed Liquidation each goes to the SushiBar |
| Liquidity Provision   | Pool             | Pair Specific Tokens    | Specific Sushi Liquidity Provider (SLP) Token | 0.25% LP Fees                                                                                  |
| KMP Farming           | Farm             | Pair Specific KMP Token | N/A                                           | Pair Specific Yield in SUSHI Token                                                             | 
| SLP Farming           | Farm             | Pair Specific SLP Token | N/A                                           | Pair Specific Yield in SUSHI Token                                                             |
| SUSHI Staking         | Stake (SushiBar) | SUSHI                   | xSUSHI                                        | 0.05% of all swaps earned in SUSHI Token                                                       |

Let us now look at each specific revenue stream that SushiSwap offers. This analysis aims to figure out the role of SUSHI Token within the Ecosystem which can help us understand the intrinsic value of holding SUSHI.

## Activities
### "Pair Isolated Lending":
Market exists for both xSUSHI and SUSHI to be put up as collateral. Users may wish to borrow on Kashi and put up SUSHI or xSUSHI as collateral to enjoy better interests rates. Kashi operates on an elastic interest rate which targets market utilization of 70% - 80%. Anything lower than the targeted range would mean that interest rates are cheaper. Borrowers might capitalize on this opportunity by buying up SUSHI (and if needed, staking for xSUSHI) to be put up as collateral to meet their needs. 

Additionally, 10% of earned interests and closed liquidations goes to the SushiBar for xSUSHI holders to enjoy. (Price-to-Earnings applies here.)

Monitoring wallet/asset activity on Kashi can give us a clue on potential demand for SUSHI to either:
1. be put up as collateral
2. to earn extra passive yields stemming from Kashi activity

Should the lending activity increase overtime, yield hunters would want to invest in SUSHI (and stake it for xSUSHI) to enjoy greater earnings.

### "Liquidity Provision":
On the macro scale, we can monitor total token swapping activity and the total LP fees generated. We can also isolate LP pools by chains for chain-to-chain analysis.  (Price-to-RevStream, Revenue-to-Locked applies here.)
Because of SushiBar, xSUSHI holders also earn a portion of these proceeds in SUSHI. (Price-to-Earnings applies here.)

On the micro scale, there exists swaps for SUSHI and xSUSHI. We can study the LP fees earned in these pairs and compare it with an entirely different LP pairs but with similar risk profiles. If the LP fees earned on SUSHI or xSUSHI pairs are more attractive (due to high trading activity) than the others, it is safe to assume that individuals with a LP strategy will want to provide liquidity in the SUSHI pairs which drives the demand for SUSHI.

### "KMP & SLP Farming": 
On the macro scale, we can calculate lending and LP related farming yields and compare it with other DeFis. (Price-to-RevStream, Revenue-to-Locked applies here.)

On the micro scale, we can compare SUSHI Token specific Lending & LP yields with another token with a similar risk profile. As stated earlier, should the yields earned be more attractive with SUSHI Tokens, then it is natural that the demand for SUSHI to increase until it reaches the market expectation.

### "SUSHI Staking": 
As of the time of writing, apart from additional swap fees earned, governance is the only other function of the xSUSHI token.

