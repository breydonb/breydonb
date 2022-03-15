import React from "react";

import { Button } from 'react-bootstrap';

const StartButton = ({ callback }) => (
    <>
        <Button variant="primary">Start Game</Button>{callback}
    </>
)

export default StartButton;