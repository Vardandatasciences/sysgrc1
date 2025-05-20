describe('Login Page Tests', () => {
  it('logs in successfully', () => {
    cy.visit('/login/');
    cy.get('input[name="actor_id"]').type('1040');
    cy.get('input[name="password"]').type('Srikar@123');
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/admin/dashboard');
  });
});
