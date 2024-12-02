import Data.List (sort)


main = do
    input <- readFile "in.txt"
    let reports = lines input
    let levels :: [[Int]] = map (map read . words) reports
    let unsafe = filter (not . isSafe) levels

    -- part 1 - count all safe
    print $ length reports - length unsafe

    -- part 2 - check unsafes to see if they can be made safe by removing a single level
    let veryUnsafes = filter (not . canBeMadeSafe) unsafe
    print $ length reports - length veryUnsafes
    

-- isSkewed is a bit of a misnomer. It just means 'is always increasing' or 'is always decreasing'
isSkewed :: [Int] -> Bool
isSkewed xs = sort xs == xs || reverse (sort xs) == xs

isGradual :: [Int] -> Bool
isGradual [] = True
isGradual [x] = True
isGradual (x:(y:ys)) = abs (x - y) >= 1 && abs (x - y) <= 3 && isGradual (y:ys)

isSafe :: [Int] -> Bool
isSafe xs = isSkewed xs && isGradual xs

canBeMadeSafe :: [Int] -> Bool
canBeMadeSafe xs = canBeMadeSafe' xs 0

canBeMadeSafe' :: [Int] -> Int -> Bool
canBeMadeSafe' [] _ = True
canBeMadeSafe' [x] _ = True
canBeMadeSafe' xs ind
    | ind >= length xs = False
    | isSafe (removeAt xs ind) = True
    | otherwise = canBeMadeSafe' xs (ind + 1)

removeAt :: [a] -> Int -> [a]
removeAt xs ind = removeAt' xs ind [] xs

removeAt' :: [a] -> Int -> [a] -> [a] -> [a]
removeAt' xs 0 lft rgt = lft ++ tail rgt
removeAt' xs ind lft rgt = removeAt' xs (ind - 1) (lft ++ [head rgt]) (tail rgt)