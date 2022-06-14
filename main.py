from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import board
print("Starting")


keyboard = KMKKeyboard()

_______ = KC.TRNS

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,
                     board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,)

keyboard.row_pins = (board.GP26, board.GP22, board.GP21,
                     board.GP20, board.GP19, board.GP18, board.GP17, board.GP16,)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        _______, _______,  KC.ESC, KC.NUBS,   KC.F4,    KC.G,   KC.F5,    KC.H,   KC.F6, _______, KC.QUOT, _______,   KC.P0, KC.PDOT,   KC.UP, KC.LGUI,
        _______, KC.LSFT,  KC.TAB, KC.CLCK,   KC.F3,    KC.T, KC.BSPC,    KC.Y, KC.RBRC,   KC.F7, KC.LBRC,   KC.P4,   KC.P5,   KC.P6, KC.PPLS, _______,
        KC.LCTL, _______,  KC.GRV,   KC.F1,   KC.F2,   KC.N5,   KC.F9,   KC.N6,  KC.EQL,   KC.F8, KC.MINS,  KC.DEL,  KC.INS, KC.PGUP, KC.HOME, _______,
        _______, _______,   KC.N1,   KC.N2,   KC.N3,   KC.N4,  KC.F10,   KC.N7,   KC.N8,   KC.N9,   KC.N0,  KC.F11,  KC.F12, KC.PGDN,  KC.END, KC.PSCR,
        _______, _______,    KC.Q,    KC.W,    KC.E,    KC.R, _______,    KC.U,    KC.I,    KC.O,    KC.P,   KC.P7,   KC.P8,   KC.P9, KC.PPLS, KC.SLCK,
        _______, _______,    KC.A,    KC.S,    KC.D,    KC.F, KC.BSLS,    KC.J,    KC.K,    KC.L, KC.SCLN,   KC.P1,   KC.P2,   KC.P3, KC.PENT, _______,
        KC.RCTL, KC.RSFT,    KC.Z,    KC.X,    KC.C,    KC.V,  KC.ENT,    KC.M, KC.COMM,  KC.DOT, KC.NUHS, KC.NLCK, KC.PSLS, KC.PAST, KC.PAUS, _______,
        _______, _______, _______, _______, _______,    KC.B,  KC.SPC,    KC.N, _______, _______, KC.SLSH, KC.DOWN, KC.RGHT, KC.PMNS, KC.LEFT, KC.RALT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
