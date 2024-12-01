import Data.List (sort)


main = do
    l <- readFile "in.txt"
    let ls = lines l
    let ps = map (pack . words) ls
    let col1 :: [Int] = map read (sort $ map fst ps)
    let col2 :: [Int] = map read (sort $ map snd ps)
    
    let ds = dists col1 col2
    print $ sum ds

    let sims = getSims col1 col2
    print $ sum sims
    

pack :: [String] -> (String, String)
pack [a, b] = (a, b)

dists :: [Int] -> [Int] -> [Int]
dists [x] [y] = [abs (x - y)]
dists (x:xs) (y:ys) = abs (x - y) : dists xs ys

similarity :: Int -> [Int] -> Int
similarity x xs = x * length ( filter (== x) xs)

getSims :: [Int] -> [Int] -> [Int]
getSims [x] ys = [similarity x ys]
getSims (x:xs) ys = similarity x ys : getSims xs ys