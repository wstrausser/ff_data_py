# Scoring models

### `model_name`
*string* -- The name of the model.

### `description`
*string* -- A brief description of the model, its source website, etc.

---

## `metadata`
All fields in this section are merely for information purposes and do not impact the scoring algorithm.

### `decimal`
*boolean* -- Indicates whether this is a decimal scoring model or not.

### `ppr`
*boolean* -- Indicates whether this is a points per reception (PPR) scoring model or not.

---

## `committed_turnovers`
Scoring parameters for committed turnovers. Values here are universal and apply to offensive, defensive, and special teams players. In the case of defenses, these values are only applied in the rare case that a defensive player **commits** a turnover, not when they **force** a turnover (forced turnovers are in the `dst` section). That is, a defensiver player making an interception and subsequently fumbling the ball on the same play will receive a point value corresponding to the `interception` field in the `dst` section, followed by an additional (usually negative) point value according to the `fumble` field in this section.

### `fumble`
*int* or *float* -- Point value awarded for a committed fumble, regardless of whether the fumble was recovered by the opposing team or not.

### `fumble_lost`
*int* or *float* -- Point value awarded for a committed lost fumble (i.e. a fumble committed by the player and then recovered by the opposing team).

### `interception`
*int* or *float* -- Point value awarded for a thrown interception.

---

## `passing`

### `yards`
*int* or *float* -- Point value awarded for every *n* passing yards (*n* = `yards_step`).

### `yards_interval`
*int* -- Interval at which a player will gain the number of points specified by `yards`. For instance, with `yards = 1` and `yards_interval = 10`, a player with 48 passing yards will earn 4 points.

### `touchdown`
*int* or *float* -- Point value awarded for every passing touchdown thrown.

## `passing.bonuses`

### `game_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for their overall passing yardage in the game (*n* = `game_yardage_bonus`). This value is inclusive.

### `game_yardage_bonus`
*int* or *float* -- Point value awarded when a player crosses the passing yardage threshold specified by `game_yardage_bonus_threshold`.

### `game_yardage_secondary_bonus_interval`
*int* -- The interval at which a player receives a bonus of *n* additional points after surpassing the passing yardage threshold specified in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus`).

### `game_yardage_secondary_bonus`
*int* or *float* -- Point value awarded for every *n* passing yards earned above the value in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus_interval`)

### `td_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for the yardage of a passing touchdown play (*n* = `td_yardage_bonus`).

### `td_yardage_bonus`
*int* or *float* -- Point value awarded for a touchdown of greater than or equal yardage to `td_yardage_bonus_threshold`, in addition to base point value awarded by `touchdown`.

---

## `receiving`

### `yards`
*int* or *float* -- Point value awarded for every *n* receiving yards (*n* = `yards_step`).

### `yards_interval`
*int* -- Interval at which a player will gain the number of points specified by `yards`. For instance, with `yards = 1` and `yards_interval = 10`, a player with 48 receiving yards will earn 4 points.

### `touchdown`
*int* or *float* -- Point value awarded for every receiving touchdown thrown.

### `reception`
*int* or *float* -- Point value awarded for each reception.

## `receiving.bonuses`

### `game_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for their overall receiving yardage in the game (*n* = `game_yardage_bonus`). This value is inclusive.

### `game_yardage_bonus`
*int* or *float* -- Point value awarded when a player crosses the receiving yardage threshold specified by `game_yardage_bonus_threshold`.

### `game_yardage_secondary_bonus_interval`
*int* -- The interval at which a player receives a bonus of *n* additional points after surpassing the receiving yardage threshold specified in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus`).

### `game_yardage_secondary_bonus`
*int* or *float* -- Point value awarded for every *n* receiving yards earned above the value in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus_interval`)

### `td_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for the yardage of a receiving touchdown play (*n* = `td_yardage_bonus`).

### `td_yardage_bonus`
*int* or *float* -- Point value awarded for a touchdown of greater than or equal yardage to `td_yardage_bonus_threshold`. Awarded in addition to base point value specified by `touchdown`.

---

## `rushing`

### `yards`
*int* or *float* -- Point value awarded for every *n* rushing yards (*n* = `yards_step`).

### `yards_interval`
*int* -- Interval at which a player will gain the number of points specified by `yards`. For instance, with `yards = 1` and `yards_interval = 10`, a player with 48 rushing yards will earn 4 points.

### `touchdown`
*int* or *float* -- Point value awarded for every rushing touchdown thrown.

## `rushing.bonuses`

### `game_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for their overall rushing yardage in the game (*n* = `game_yardage_bonus`). This value is inclusive.

### `game_yardage_bonus`
*int* or *float* -- Point value awarded when a player crosses the rushing yardage threshold specified by `game_yardage_bonus_threshold`.

### `game_yardage_secondary_bonus_interval`
*int* -- The interval at which a player receives a bonus of *n* additional points after surpassing the rushing yardage threshold specified in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus`).

### `game_yardage_secondary_bonus`
*int* or *float* -- Point value awarded for every *n* rushing yards earned above the value in `game_yardage_bonus_threshold` (*n* = `game_yardage_secondary_bonus_interval`)

### `td_yardage_bonus_threshold`
*int* -- The threshold where a player receives a bonus of *n* points for the yardage of a rushing touchdown play (*n* = `td_yardage_bonus`).

### `td_yardage_bonus`
*int* or *float* -- Point value awarded for a touchdown of greater than or equal yardage to `td_yardage_bonus_threshold`. Awarded in addition to base point value specified by `touchdown`.

---

## `kicking`

### `field_goal`
*int* or *float* -- Point value awarded for a successful field goal attempt.

### `field_goal_yards`
*int* or *float* -- Point value awarded for every *n* yards of distance for a successful kick (*n* = `field_goal_yards_interval`).

### `field_goal_yards_interval`
*int* -- Interval at which points are awarded for `field_goal_yards`. For instance, with `field_goal = 0.1`, `field_goal_yards = 0.1`, and `field_goal_yards_interval = 1`, a successful field goal attempt of 48 yards will earn *0.1 + (0.1 \* 48) = 4.9* points.

### `field_goal_miss`
*int* or *float* -- Point value awarded for an unsuccessful field goal attempt up to a distance of `field_goal_miss_max_yards`.

### `field_goal_miss_max_yards`
*int* -- Maximum kick yardage for which *n* points will be awarded for a missed field goal (inclusive). For instance, with `field_goal_miss = -1` and `field_goal-miss_max_yards = 49`, a missed kick of 49 or fewer yards will be penalized -1 point, while a missed kick of 50 yards will receive no penalty.

### `extra_point`
*int* or *float* -- Point value awarded for a successful extra point.

### `extra_point_miss`
*int* or *float* -- Point value awarded for an unsuccessful extra point.

---

## `dst`
Scoring parameters for team-based defense/special teams scoring.

## `dst.defense`

### `touchdown`
*int* or *float* -- Point value awarded for a defensive touchdown (on either an interception or fumble return).

### `safety`
*int* or *float* -- Point value awarded for a safety scored by defense.

### `sack`
*int* or *float* -- Point value awarded for a sack.

### `forced_fumble`
*int* or *float* -- Point value awarded for a forced fumble.

### `fumble_recovery`
*int* or *float* -- Point value awarded for a fumble recovery.

### `interception`
*int* or *float* -- Point value awarded for a defensive interception.

### `tackle_for_loss`
*int* or *float* -- Point value awarded for a tackle for loss.

### `pass_defended`
*int* or *float* -- Point value awarded for a pass defended.

### `two_point_return`
*int* or *float* -- Point value awarded for returning a two-point conversion attempt to the offensive team's endzone.

### `points_allowed`
*inline table* -- Defines the ranges for awarding points based on defensive points allowed. Each row in the table must contain the following three values: `range_min`, `range_max`, and `points`. For instance, if the table includes the row `{ range_min = 18, range_max = 21, points = 0.25 }`, a defense allowing 20 points in a game will be awarded 0.25 fantasy points. `range-min` and `range-max` are both inclusive.

### `points_allowed_deduction_threshold`
*int* -- Defines the threshold from which defenses will be deducted fantasy points for points allowed above the threshold.

### `points_allowed_deduction_interval`
*int* -- Defines the interval at which points will be deducted above the `points_allowed_deduction_threshold`.

### `points_allowed_deduction`
*int* or *float* -- Point value awarded (deducted) for every *n* defensive points allowed above the `points_allowed_deduction_threshold` (*n* = `points_alowed_deduction_interval`).

### `yards_allowed`
*inline table* -- Defines the ranges for awarding points based on defensive yards allowed. Each row in the table must contain the following three values: `range_min`, `range_max`, and `points`. For instance, if the table includes the row `{ range_min = 206, range_max = 210, points = 1.9 }`, a defense allowing 208 yards in a game will be awarded 1.9 fantasy points. `range-min` and `range-max` are both inclusive.

### `points_allowed_deduction_threshold`
*int* -- Defines the threshold from which defenses will be deducted fantasy points for yards allowed above the threshold.

### `yards_allowed_deduction_interval`
*int* -- Defines the interval at which points will be deducted above the `yards_allowed_deduction_threshold`.

### `yards_allowed_deduction`
*int* or *float* -- Point value awarded/deducted for every *n* yards allowed above the `yards_allowed_deduction_threshold` (*n* = `yards_alowed_deduction_interval`).

## `dst.special_teams`

### `kick_return_td`
*int* or *float* -- Point value awarded for each kick return touchdown.

### `punt_return_td`
*int* or *float* -- Point value awarded for each punt return touchdown.

### `extra_point_return`
*int* or *float* -- Point value awarded for returning an extra point attempt to the kicking team's endzone.

### `blocked_field_goal`
*int* or *float* -- Point value awarded for blocking a field goal attempt.

### `blocked_extra_point`
*int* or *float* -- Point value awarded for blocking an extra point attempt.

### `blocked_punt`
*int* or *float* -- Point value awarded for blocking a punt.