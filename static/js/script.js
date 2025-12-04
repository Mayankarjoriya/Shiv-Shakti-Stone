// Custom Cursor
const cursor = document.querySelector('.cursor');
const follower = document.querySelector('.cursor-follower');

let timeout;

document.addEventListener('mousemove', (e) => {
    if (!cursor || !follower) return;

    const x = e.clientX;
    const y = e.clientY;

    cursor.style.left = `${x}px`;
    cursor.style.top = `${y}px`;

    requestAnimationFrame(() => {
        follower.style.left = `${x}px`;
        follower.style.top = `${y}px`;
    });
    
    clearTimeout(timeout);
    cursor.style.width = '20px';
    cursor.style.height = '20px';
    follower.style.width = '40px';
    follower.style.height = '40px';

    timeout = setTimeout(() => {
        cursor.style.width = '6px';
        cursor.style.height = '6px';
        follower.style.width = '20px';
        follower.style.height = '20px';
    }, 100);
});

// Hover effect for links and buttons
const hoverElements = document.querySelectorAll('button, .btn, a');
hoverElements.forEach(button => {
    button.addEventListener('mouseenter', () => {
        if(follower) {
            follower.style.width = '50px';
            follower.style.height = '50px';
        }
    });
    button.addEventListener('mouseleave', () => {
        if(follower) {
            follower.style.width = '20px';
            follower.style.height = '20px';
        }
    });
});

// Ripple effect on buttons
document.querySelectorAll('button, .btn').forEach(button => {
    button.addEventListener('click', function(e) {
        
        const x = e.clientX - e.target.getBoundingClientRect().left;
        const y = e.clientY - e.target.getBoundingClientRect().top;
        
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// Mobile Menu Toggle
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navMenu = document.querySelector('.nav-menu');

mobileMenuBtn.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
            navMenu.classList.remove('active');
        }
    });
}); 

// Scroll animations
const fadeElements = document.querySelectorAll('.fade-in');

const appearOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -100px 0px"
};

const appearOnScroll = new IntersectionObserver((entries, appearOnScroll) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            entry.target.classList.add('appear');
            appearOnScroll.unobserve(entry.target);
        }
    });
}, appearOptions);

fadeElements.forEach(element => {
    appearOnScroll.observe(element);
});

// Parallax effect on hero image
document.addEventListener('mousemove', (e) => {
    const heroImage = document.querySelector('.hero-image img');
    if (!heroImage) return;

    if (document.querySelector('.hero-image:hover')) {
        heroImage.style.transform = 'perspective(1000px) rotateY(0deg)';
        return;
    }
    
    const x = (e.pageX - (window.innerWidth / 2)) / 50;
    const y = (e.pageY - (window.innerHeight / 2)) / 50;
    
    const xRot = Math.max(-10, Math.min(10, -y * 0.5));
    const yRot = Math.max(-10, Math.min(10, x * 0.5));

    heroImage.style.transform = `perspective(1000px) rotateX(${xRot}deg) rotateY(${yRot}deg)`;
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if(targetId === '#') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
            return;
        }
        
        const targetElement = document.querySelector(targetId);
        if(targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80, // Offset for fixed header
                behavior: 'smooth'
            });
        }
    });
});

// Product Filter Sidebar Toggle
const filterToggleBtn = document.getElementById('filter-toggle-btn');
const filterSidebar = document.getElementById('filter-sidebar');
const closeFiltersBtn = document.getElementById('close-filters-btn');
const filterOverlay = document.getElementById('filter-overlay');

if (filterToggleBtn && filterSidebar && closeFiltersBtn && filterOverlay) {
    const toggleFilters = () => {
        filterSidebar.classList.toggle('open');
        filterOverlay.classList.toggle('open');
    };

    filterToggleBtn.addEventListener('click', toggleFilters);
    closeFiltersBtn.addEventListener('click', toggleFilters);
    filterOverlay.addEventListener('click', toggleFilters);
}