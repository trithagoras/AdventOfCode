import Data.List (sort)


main = do
    input <- readFile "in.txt"
    let reports = lines input
    let levels :: [[Int]] = map (map read . words) reports
    let safe = length $ filter (== True) $ map isSafe levels
    print safe

-- isSkewed is a bit of a misnomer. It just means 'is always increasing' or 'is always decreasing'
isSkewed :: [Int] -> Bool
isSkewed xs = sort xs == xs || reverse (sort xs) == xs

isGradual :: [Int] -> Bool
isGradual [] = True
isGradual [x] = True
isGradual (x:(y:ys)) = abs (x - y) >= 1 && abs (x - y) <= 3 && isGradual (y:ys)

isSafe :: [Int] -> Bool
isSafe xs = isSkewed xs && isGradual xs