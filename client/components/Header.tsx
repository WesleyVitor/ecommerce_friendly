import {FC} from 'react'
import React, {useState} from 'react'
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

export const Header: FC = ()=>{
    const [collapsed, setCollapsed] = useState(true);

    const toggleNavbar = () => setCollapsed(!collapsed);
    return (        
        <Navbar color="primary" light>
            <NavbarBrand href="/" className="me-auto">
            Ecommerce Friendly
            </NavbarBrand>
            <NavbarToggler onClick={toggleNavbar} className="me-2" />
            <Collapse isOpen={!collapsed} navbar>
            <Nav navbar>
                <NavItem>
                <NavLink href="/">Components</NavLink>
                </NavItem>
                <NavItem>
                <NavLink href="https://github.com/reactstrap/reactstrap">
                    Login
                </NavLink>
                </NavItem>
            </Nav>
            </Collapse>
        </Navbar>
        
    )
}


