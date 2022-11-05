# Scoring models

### `model_name`
*string* -- The name of the model.

### `description`
*string* -- A brief description of the model, its source website, etc.

## `metadata`
All fields in this section are merely for information purposes and do not impact the scoring algorithm.

### `decimal`
*boolean* -- Indicates whether this is a decimal scoring model or not.

### `ppr`
*boolean* -- Indicates whether this is a points per reception (PPR) scoring model or not.

## `committed_turnovers`
Point values for committed turnovers. Values here are universal and apply to offensive, defensive, and special teams players. In the case of defenses, these values are only applied in the rare case that a defensive player **commits** a turnover, not when they **force** a turnover (forced turnovers are in the `dst` section). That is, a defensiver player making an interception and subsequently fumbling the ball on the same play will receive a point value corresponding to the `interception` field in the `dst` section, followed by an additional (usually negative) point value according to the `fumble` field in this section.

### `fumble`
*int* or *float* -- Point value awarded for a committed fumble, regardless of whether the fumble was recovered by the opposing team or not.

### `fumble_lost`
*int* or *float* -- Point value awarded for a committed lost fumble (i.e. a fumble committed by the player and then recovered by the opposing team).

### `interception`
*int* or *float* -- Point value awarded for a thrown interception.

## `passing`

### `yards`
*int* or *float* -- Point value awarded for every *n* passing yards (*n* = `yards_step`).

### `yards_interval`
*int* -- Interval at which a player will gain the number of points specified by `yards`. That is, for `yards = 1` and `yards_interval = 10`, a player with 48 yards will earn 4 points.

### `touchdown`
*int* or *float* -- Point value awarded for every passing touchdown thrown.

## `passing.bonuses`

### `game_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for their overall passing yardage in the game (*n* = `game_yardage_bonus`). This value is inclusive.

### `game_yardage_bonus`
*int* or *float* -- Point value awarded when a player crosses the passing yardage mark specified by `game_yardage_bonus_threshold`.

### `game_yardage_secondary_bonus_interval`
*int* -- The interval at which a player receives a bonus of *n* additional points after surpassing the passing yardage threshold specified in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus`).

### `game_yardage_secondary_bonus`
*int* or *float* -- Point value awarded for every *n* passing yards earned above the value in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus_interval`)

### `td_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for the yardage of a passing touchdown play (*n* = `td_yardage_bonus`).

### `td_yardage_bonus`
*int* or *float* -- Point value awarded for a touchdown of greater than or equal yardage to `td_yardage_bonus_threshold`, in addition to base point value awarded by `touchdown`.