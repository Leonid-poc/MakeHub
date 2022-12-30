import NavLinks from "./NavLinks";
import classes from './Navbar.module.css';
import { CgMenuRound, CgCloseO } from 'react-icons/cg';
import { useState } from 'react';

const MobileNavigation = () => {

    const [open, setOpen] = useState(false);
    
    const HamburgerIcon = <CgMenuRound  className={classes.Hamburger}  size='40px' color='#ffffffb3' onClick={() => setOpen(!open)} />;
    const CloseIcon = <CgCloseO  className={classes.Hamburger}  size='40px' color='#ffffffb3' onClick={() => setOpen(!open)} />;
    const closeMobileMeny = () => setOpen(false);

    return (
        <nav className={classes.MobileNavigation}>
            {open ? CloseIcon : HamburgerIcon}
            {open && <NavLinks isMobile={true} closeMobileMenu={closeMobileMeny} />}
        </nav>
    );
}
    
export default MobileNavigation
