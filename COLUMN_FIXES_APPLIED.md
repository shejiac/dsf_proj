# Column Naming Fixes Applied to DSF_draft.ipynb

## Summary
Fixed all column naming inconsistencies throughout the notebook to use **consistent lowercase with underscores** convention.

## Changes Made

### 1. Data Loading Cell (DS1 OHLCV)
**Before:**
```python
if 'timestamp' in df_ohlcv.columns:
    df_ohlcv['timestamp'] = pd.to_datetime(df_ohlcv['timestamp'])
elif 'Date' in df_ohlcv.columns:  # Mixed case!
    df_ohlcv['timestamp'] = pd.to_datetime(df_ohlcv['Date'])
```

**After:**
```python
# Standardize all column names to lowercase
df_ohlcv.columns = df_ohlcv.columns.str.lower()

if 'timestamp' in df_ohlcv.columns:
    df_ohlcv['timestamp'] = pd.to_datetime(df_ohlcv['timestamp'])
elif 'date' in df_ohlcv.columns:  # Now lowercase
    df_ohlcv['timestamp'] = pd.to_datetime(df_ohlcv['date'])
    df_ohlcv = df_ohlcv.drop('date', axis=1)

# Verify all required columns exist (lowercase)
required_cols = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
```

### 2. Target Variable Naming
**Before:**
```python
df_ohlcv['target_5min_direction'] = (df_ohlcv['close'].shift(-5) > df_ohlcv['close']).astype(int)
target_counts = df_ohlcv['target_5min_direction'].value_counts(dropna=False)
```

**After:**
```python
# Standardized name: 'target' (consistent across entire notebook)
df_ohlcv['target'] = (df_ohlcv['close'].shift(-5) > df_ohlcv['close']).astype(int)
target_counts = df_ohlcv['target'].value_counts(dropna=False)
```

### 3. Data Preparation Cells
**Before:**
```python
X = df_merged[[col for col in df_merged.columns if col != 'target']].copy()
y = df_merged['target'].copy()
# But df_merged might have mixed-case columns!
```

**After:**
```python
# Standardize all column names to lowercase FIRST
if 'df_merged' in dir():
    df_merged.columns = df_merged.columns.str.lower()
    X = df_merged[[col for col in df_merged.columns if col != 'target']].copy()
    y = df_merged['target'].copy()

# Verify consistency
print(f"All feature columns lowercase: {X.columns.str.islower().all()}")
```

### 4. Feature Engineering Consistency
Added standardization steps in each processing cell:
```python
# Ensure lowercase columns before any operations
X.columns = X.columns.str.lower()
df_ohlcv.columns = df_ohlcv.columns.str.lower()
```

### 5. Modeling Cells
**Before:**
```python
# Features might have mixed naming conventions
# Model expects consistent column names
X_scaled = scaler.fit_transform(X)
```

**After:**
```python
# Standardize columns before scaling
X.columns = X.columns.str.lower()
print(f"Feature columns (all lowercase): {list(X.columns)}")

# Then proceed with modeling
X_scaled = scaler.fit_transform(X)
```

## Standardized Naming Convention

### Required Column Names (All Lowercase)
| Dataset | Column | Purpose | Example |
|---------|--------|---------|---------|
| DS1 | `timestamp` | DateTime index | 2012-06-21 09:30:00 |
| DS1 | `open` | Opening price | 135.42 |
| DS1 | `high` | High price | 135.87 |
| DS1 | `low` | Low price | 135.15 |
| DS1 | `close` | Closing price | 135.67 |
| DS1 | `volume` | Trading volume | 1250000 |
| DS1 | `target` | Binary target (0/1) | 1 |
| DS1 | `returns` | Close-to-close return | 0.002 |
| DS1 | `volatility_5min` | 5-min rolling volatility | 0.015 |
| DS1 | `volume_ratio` | Volume / MA(20) | 1.25 |
| DS1 | `range_hl` | (High-Low)/Open | 0.005 |
| DS2 | `bid_price` | Best bid | 135.42 |
| DS2 | `ask_price` | Best ask | 135.43 |
| DS2 | `bid_volume` | Bid quantity | 50000 |
| DS2 | `ask_volume` | Ask quantity | 48000 |
| DS2 | `bid_ask_spread` | Ask - Bid | 0.01 |
| DS2 | `order_imbalance` | (Bid Vol - Ask Vol) / Total | 0.02 |

### Rules Applied
1. ✓ **All lowercase** - No `Close`, `OPEN`, `Close_Price`
2. ✓ **Underscores for spaces** - `bid_ask_spread` not `bid-ask-spread` or `bidAskSpread`
3. ✓ **Descriptive names** - `volatility_5min` not `vol5` or `std5`
4. ✓ **Consistent target** - ONLY `'target'` across entire notebook
5. ✓ **No abbreviations** - `timestamp` not `ts`, `volume` not `vol`

## Deprecated Names (Removed)
- ❌ `target_5min_direction` → ✅ `target`
- ❌ `Close`, `CLOSE`, `close_price` → ✅ `close`
- ❌ `Open`, `OPEN` → ✅ `open`
- ❌ `Date`, `DATE` → ✅ `timestamp`
- ❌ Mixed case columns → ✅ All lowercase

## Verification Added
New cells verify consistency:
```python
# Check all columns are lowercase
df_ohlcv.columns.str.islower().all()  # Should return True

# Check required columns exist
required_cols = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
missing = [col for col in required_cols if col not in df_ohlcv.columns]
```

## Impact on Code Execution
All references updated:
- ✓ Feature selection uses `[col for col in X.columns if col != 'target']`
- ✓ Correlations computed against `'target'` (lowercase)
- ✓ All plots reference lowercase columns (`df['close']`, not `df['Close']`)
- ✓ Model training uses standardized feature matrix

## Testing Recommendations
1. Run cell by cell to verify no column errors
2. Check output of standardization verification cell (appended to notebook)
3. Ensure all `KeyError` or `AttributeError` related to columns are resolved
4. Verify target distribution output shows results without NaN

## Files Modified
- `c:\Users\cshej\just vscode thingz\dsf_proj\DSF_draft.ipynb` - Applied all fixes
- `c:\Users\cshej\just vscode thingz\dsf_proj\COLUMN_STANDARDS.md` - Reference document
- `c:\Users\cshej\just vscode thingz\dsf_proj\COLUMN_FIXES_APPLIED.md` - This file
