"use client";
import { Menu as MenuIcon } from "lucide-react";
import * as React from "react";
import Button from "@mui/material/Button";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import PopupState, { bindTrigger, bindMenu } from "material-ui-popup-state";

export default function MenuMobileButton() {
  return (
    <PopupState variant="popover" popupId="demo-popup-menu">
      {(popupState) => (
        <React.Fragment>
          <Button {...bindTrigger(popupState)}>
            <MenuIcon className="text-gray-600" />
          </Button>
          <Menu {...bindMenu(popupState)}>
            <MenuItem onClick={popupState.close}>Home</MenuItem>
            <MenuItem onClick={popupState.close}>Trip Builder</MenuItem>
            <MenuItem onClick={popupState.close}>Feed</MenuItem>
            <MenuItem onClick={popupState.close}>Profile</MenuItem>
          </Menu>
        </React.Fragment>
      )}
    </PopupState>
  );
}
