import Data.Text (splitOn, pack, unpack)
import Data.String (fromString)
import Data.Char (ord)

main = do
    s <- readFile "in.txt"
    let ts = splitOn (pack ",") (pack s)
    let ss = map unpack ts
    print $ hashStrs ss 0

hashStrs :: [String] -> Int -> Int
hashStrs ss x = sum $ map (hashStr x) ss

hashStr :: Int -> String -> Int
hashStr = foldl hashChar

hashChar :: Int -> Char -> Int
hashChar x c = (17 * (ord c + x)) `mod` 256