import Data.Text (pack, splitOn)

main :: IO ()
main = do
    s <- readFile "in.txt"
    let lines = splitOn (pack "\n") (pack s)
    print $ head lines 