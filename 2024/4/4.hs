
-- was unable to do it in haskell :(
-- wanted to do a sliding window solution but brain hurt due to recursion
-- so swapped to python for this week instead

main = do
    f <- readFile "input.txt"
    let ls = lines f
    print ls

window = ["XMAS", "....", "....", "...."]

-- match2 :: Eq a => [[a]] -> [[a]] -> (Int, Int) -> Maybe ()
-- match2 src window (row, col)
--     | length window > length src = Nothing
--     | otherwise = 

-- match :: src -> window -> (row, col)
match :: Eq a => [a] -> [a] -> Int-> Maybe ()
match src window n
    | length window > length src = Nothing
    | null window || null src = Just ()
    | head src == head window = match (tail src) (tail window) (n + 1)
    | otherwise = Nothing


safeAt2 :: [[a]] -> (Int, Int) -> Maybe a
safeAt2 src (row, col) = do
    r <- safeAt src row
    safeAt r col

safeAt :: [a] -> Int -> Maybe a
safeAt [] _ = Nothing
safeAt (x:xs) 0 = Just x
safeAt (x:xs) n
    | n < 0 = Nothing
    | otherwise = safeAt xs (n - 1)