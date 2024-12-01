import Data.Text (splitOn, pack, unpack)
import Data.String (fromString)
import Data.Char (ord)

maxRed = 12
maxGreen = 13
maxBlue = 14

data Round = R Int Int Int

main = do
    s <- readFile "in.txt"
    let ts = splitOn (pack "\n") (pack s)
    let lines = map unpack ts
    print $ head lines

-- mapping of game number -> Game, where Game contains a list of Rounds, where a Round contains x green y blue z red