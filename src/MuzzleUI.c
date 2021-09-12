#define MUZZLE_DEPS
#include <Muzzle.h>
#include "../include/MuzzleUI.h"

void MuzzleUI_SetStyle(MuzzleUI_Style style)
{
    __style = style;
}

MuzzleUI_Style MuzzleUI_GetStyle()
{
    return __style;
}

void MuzzleUI_DrawButton(MuzzleUI_Button button)
{
    tint color;

    // TODO: Add Borders (Already in struct)

    switch (button.status)
    {
    case DISABLED:
        color = __style.rectangle.disabled.color;
        break;

    case PRESSED:
        color = __style.rectangle.pressed.color;

    case HOVER:
        color = __style.rectangle.hover.color;

    case REGULAR:
        color = __style.rectangle.regular.color;
    
    default:
        color = __style.rectangle.regular.color;
        break;
    }

    draw_rectangle(button.collider.x, button.collider.y, button.collider.width - MZ_UI_COLLIDER_BUFFER_AREA, button.collider.height - MZ_UI_COLLIDER_BUFFER_AREA, color);
}

void MuzzleUI_UpdateButton(MuzzleUI_Button* button, Applet* applet)
{
    if (__mzui_internal_check_collision_point_rec(get_mouse_position_vec2(applet), button->collider) && button->status != DISABLED) button->status = HOVER;
    if (button->status == HOVER, mouse_down(applet, MOUSE_LEFT)) button->status = PRESSED;
    
    else if (button->status != DISABLED) button->status = REGULAR;
}