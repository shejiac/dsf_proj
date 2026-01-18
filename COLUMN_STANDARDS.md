# Column Naming Standards for DSF_draft.ipynb

## Standardized Column Names (FINAL)

### From DS1: SPY OHLCV Data
- `timestamp` - datetime index
- `open` - opening price (lowercase)
- `high` - high price (lowercase)
- `low` - low price (lowercase)
- `close` - closing price (lowercase)
- `volume` - trading volume (lowercase)
- `returns` - close-to-close returns
- `volatility_5min` - 5-minute rolling volatility
- `volume_ma_20` - 20-period moving average of volume
- `volume_ratio` - volume / volume_ma_20
- `range_hl` - (high-low)/open range
- `valid_ohlc` - boolean validity check
- `intra_minute_vol` - high minus low
- `target` - binary target (0=down, 1=up) at 5-minute horizon

### From DS2: LOBSTER Order Book (when available)
- `bid_price` - best bid price
- `bid_volume` or `bid_size` - best bid quantity
- `ask_price` - best ask price
- `ask_volume` or `ask_size` - best ask quantity
- `bid_ask_spread` - ask_price - bid_price
- `order_imbalance` - (bid_volume - ask_volume) / total
- `depth_level1` - bid_volume + ask_volume
- `depth_imbalance` - (bid_volume - ask_volume) / depth_level1
- `mid_price` - (bid_price + ask_price) / 2
- `realized_volatility` - rolling volatility from order book

### From DS3: FRED Sentiment/Regime Data
- `stress_index` - Federal Reserve Financial Stress Index
- `regime` - market regime classification

### Merged DataFrame (df_merged)
- All columns from above three datasets
- MUST use consistent lowercase naming convention
- NO CamelCase or mixed naming

## Column Naming Rules
1. **Always lowercase** - Never use 'Close', 'Open', 'VOLUME', etc.
2. **Underscores for spaces** - Use `bid_ask_spread`, not `bid-ask-spread` or `bidAskSpread`
3. **No abbreviations** - Use `timestamp`, not `ts` or `time_idx`
4. **Descriptive names** - Use `volatility_5min`, not `vol5` or `std5`
5. **Consistent target** - ONLY use 'target', never 'target_5min_direction', 'direction', 'label', etc.

## Depreciated Names (REMOVE these)
- ❌ `target_5min_direction` → ✅ `target`
- ❌ `Close`, `Close_Price` → ✅ `close`
- ❌ `Open_Price`, `OPEN` → ✅ `open`
- ❌ `High_Price`, `HIGH` → ✅ `high`
- ❌ `Low_Price`, `LOW` → ✅ `low`
- ❌ `Trading_Volume`, `VOLUME` → ✅ `volume`
- ❌ `Ask_Price[1]`, `Ask Price 1` → ✅ `ask_price`
- ❌ `Bid_Volume[1]`, `Bid Volume 1` → ✅ `bid_volume`

## Verification Code
```python
# Run this to verify all columns are lowercase
required_lowercase = df_merged.columns.str.islower().all()
if not required_lowercase:
    mixed_case_cols = df_merged.columns[~df_merged.columns.str.islower()].tolist()
    print(f"ERROR: Non-lowercase columns found: {mixed_case_cols}")
    df_merged.columns = df_merged.columns.str.lower()
    print("Columns converted to lowercase")
```

## Impact on Code Cells
- **Explore cells**: Use `df_ohlcv['close']`, not `df_ohlcv['Close']`
- **Process cells**: Reference `df['returns']`, not `df['RETURNS']`
- **Model cells**: Select features with `X.columns`, all lowercase
- **Output cells**: Print `df.columns` to verify consistency

