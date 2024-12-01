import Data.Text (splitOn, pack)


main :: IO ()
main = do
    s <- readFile "in.txt"
    let ss = splitOn (pack "\n") (pack s)
    print $ head ss