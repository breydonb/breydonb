export const TETROMINOS = {
    0: { shape: [[0]], color: '0, 0, 0'},
    I: {
        shape:  [
                    [0, 'I', 0, 0],
                    [0, 'I', 0, 0],
                    [0, 'I', 0, 0],
                    [0, 'I', 0, 0]
                ],
        color: '0, 255, 255'
            
    },
    L: {
        shape:  [
                    [0, 'L', 0],
                    [0, 'L', 0],
                    [0, 'L', 'L']
                ],
        color: '223, 173, 36'
            
    },
    T: {
        shape:  [
                    [0, 0, 0],
                    ['T', 'T', 'T'],
                    [0, 'T', 0]
                ],
        color: '132, 61, 192'
            
    },
    J: {
        shape:  [
                    [0, 'J', 0],
                    [0, 'J', 0],
                    ['J', 'J', 0]
                ],
        color: '32, 95, 223'
            
    },
    O: {
        shape:  [
                    ['O', 'O'],
                    ['O', 'O']
                ],
        color: '223, 217, 32'
            
    },
    S: {
        shape:  [
                    ['S', 'S', 0],
                    [0, 'S', 'S'],
                    [0, 0, 0]
                ],
        color: '223, 217, 32'
            
    },
    Z: {
        shape:  [
                    ['Z', 'Z', 0],
                    [0, 'Z', 'Z'],
                    [0, 0, 0]
                ],
        color: '227, 78, 78'
            
    }

}

export const randomTetromino = () => {
    const tetrominos = 'ILTJOSZ';
    const randTetromino = tetrominos[Math.floor(Math.random() * tetrominos.length)];

    return TETROMINOS[randTetromino]
}