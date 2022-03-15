export const STAGE_WIDTH = 12;
export const STAGE_HEIGHT = 20;

export const createStage = () =>
    Array.from(Array(STAGE_HEIGHT), () =>
        // 0 means there is nothing while 'clear' clears the cell
        new Array(STAGE_WIDTH).fill([0, 'clear'])
    )