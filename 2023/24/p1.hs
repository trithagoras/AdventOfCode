import Data.Text (splitOn, pack)

main :: IO ()
main = do
    f <- readFile "in.txt"
    let lines = splitOn (pack "\n") (pack f)
    print $ head lines