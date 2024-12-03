import Data.Char (isDigit, isAlpha)

data Token = Mul | LeftParen | Comma | RightParen | Number Int | EOF | NoOp deriving (Show, Eq)

data Node = MulNode Int Int deriving (Show, Eq)

-- This solution is absolutely overkill.
-- I could have very simply just used regex for example, but wanted to make it a bit more fun

main = do
    f <- readFile "input.txt"
    let input :: String = concat $ lines f
    let tokens = scanTokens input
    let nodes = program tokens
    -- print tokens
    -- print nodes
    print $ execute nodes

-- execution
execute :: [Node] -> Int
execute [] = 0
execute ((MulNode n m):nodes) = (n * m) + execute nodes

-- Parser
program :: [Token] -> [Node]
program [] = []
program (Mul:xs) = case multiply (take 6 (Mul:xs)) of
        Just node -> node : program xs
        Nothing -> program xs
program (x:xs) = program xs
    

multiply :: [Token] -> Maybe Node
multiply [Mul, LeftParen, Number n, Comma, Number m, RightParen] = Just $ MulNode n m
multiply stream = Nothing

-- Lexing

scanTokens :: String -> [Token]
scanTokens source = scanTokens' source 0 0 []

scanTokens' :: String -> Int -> Int -> [Token] -> [Token]
scanTokens' source start current acc
    | isAtEnd source current = acc ++ [EOF]
    | otherwise = case scanToken source start current of
        (Just EOF, _) -> acc ++ [EOF]
        (Just t, len) -> scanTokens' source (start + len) (start + len) (acc ++ [t])
        (Nothing, len) -> scanTokens' source (start + len) (start + len) acc


scanToken :: String -> Int -> Int -> (Maybe Token, Int)
scanToken source start current =
    let word = slice start current source in
    let next = peekNext source current in
    case word of
        "" -> (Just EOF, 0)
        "," -> (Just Comma, 1)
        "(" -> (Just LeftParen, 1)
        ")" -> (Just RightParen, 1)
        "mul(" -> (Just Mul, 3)
        (c:_)
            | isAlpha c -> scanIdentifier source start current
            | isDigit c -> scanNumber source start current
            | otherwise -> (Just NoOp, length word)

scanNumber :: String -> Int -> Int -> (Maybe Token, Int)
scanNumber source start current =
    let word = slice start current source in
    let next = peekNext source current in
    case next of
        Just c
            | isDigit c -> scanNumber source start (current + 1)
            | otherwise -> (Just (Number (read word)), length word)
        Nothing -> (Just NoOp, length word)

scanIdentifier :: String -> Int -> Int -> (Maybe Token, Int)
scanIdentifier source start current =
    let word = slice start current source in
    let next = peekNext source current in
    case next of
        Just c
            | isAlpha c -> scanIdentifier source start (current + 1)
            | otherwise -> case word of
                "mul" -> (Just Mul, 3)
                _ -> (Just NoOp, length word)
        Nothing -> (Just NoOp, length word)

slice :: Int -> Int -> [a] -> [a]
slice from to xs = take (to - from + 1) (drop from xs)

isAtEnd :: [a] -> Int -> Bool
isAtEnd source current = current >= length source

safeLast :: [a] -> Maybe a
safeLast [] = Nothing
safeLast xs = Just $ last xs

peekNext :: [a] -> Int -> Maybe a
peekNext source index
    | index + 1 >= length source = Nothing
    | otherwise = Just $ source !! (index + 1)