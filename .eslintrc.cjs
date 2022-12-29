module.exports = {
  env: {
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 9,
  },
  plugins: ['@typescript-eslint', 'unicorn'],
  rules: {
    '@typescript-eslint/camelcase': 'off',
    '@typescript-eslint/no-non-null-assertion': 'off',
    'arrow-body-style': ['error', 'as-needed'],
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'no-return-await': 'error',
    'object-shorthand': 'error',
    'unicorn/prefer-ternary': 'error',
    eqeqeq: 'error',
  },
}
