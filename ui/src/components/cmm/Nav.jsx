import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import { Link, useHistory } from 'react-router-dom'
import AccountCircle from '@material-ui/icons/AccountCircle';
// import InputBase from '@material-ui/core/InputBase';
import { fade, makeStyles } from '@material-ui/core/styles';
import MenuIcon from '@material-ui/icons/Menu';
import Button from '@material-ui/core/Button';
// import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  toolbar: {
    // background: '#D5D8DC'
    background: 'white'
  },

  title: {
    display: 'none',
    color: 'black',
    // textDecoration: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'inline-block',
    },
  },

  dayoungTitle: {
    fontsize: '1.25 rem',
    textDecoration: 'none',
    color: 'black',
  },

  link: {
    fontsize: '1 rem',
    textDecoration: 'none',
    color: 'black'
  },

  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(1),
      width: 'auto',
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      width: '12ch',
      '&:focus': {
        width: '20ch',
      },
    },
  },
}));

export default function Nav(props) {
  const classes = useStyles();
  const history  = useHistory()
    const logout = e => {
        alert('logout')
        e.preventDefault();
        sessionStorage.removeItem("sessionUser")
        history.push('/')
        window.location.reload()
    }
  return (
    <div className={classes.root}>
      <AppBar position="static">
       <Toolbar className={classes.toolbar}>
       {props.isAuth !== null
        ? <div>  
          <Button style ={{fontSize: 25}}>
            <Link to="/" className={classes.dayoungTitle}>다영이</Link>
            </Button>
        {/* <Typography style={{ paddingLeft: 20 }}> */}
          <Button>
            <Link to="/userregister" className={classes.link}>회원 가입</Link>
          </Button>
          <Button onClick = {logout}>
            로그아웃
            {/* <Link to="/userlogin" className={classes.link}>로그아웃</Link> */}
          </Button>
          <Button>
            <Link to="/actorquiz" className={classes.link}>배우</Link>
          </Button>
          <Button>
            <Link to="/review-container" className={classes.link}>리뷰</Link>
          </Button>
          <Link to="/userprofile" className={classes.link}>
            <IconButton
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              color="inherit"
            >
              <AccountCircle/>
            </IconButton>
          </Link>
        {/* </Typography> */}
        </div>:
          <div>
          {/* <Typography className={classes.title} variant="h6" noWrap> */}
          <Button style ={{fontSize: 25}}>
            <Link to="/" className={classes.dayoungTitle}>다영이</Link>
            </Button>
        {/* </Typography>  */}
          {/* <Button>
          <Link to="/userregister" className={classes.link}>회원 가입</Link>
        </Button>
        <Button>
          <Link to="/userlogin" className={classes.link}>로그인</Link>
        </Button> */}
        </div>
      }  
        </Toolbar>
     
      </AppBar>
    </div >
  );
}